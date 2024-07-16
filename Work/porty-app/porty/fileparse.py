# fileparse.py
#
# Exercise 3.3
import csv
import logging
log = logging.getLogger(__name__)


def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=True):
    '''
    parse a csv file into list of record
    '''
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")
    rows = csv.reader(lines, delimiter=delimiter)
    if has_headers:
        headers = next(rows)
    else:
        headers = []
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    records = []
    for rowno, row in enumerate(rows, start=1):
        if not row:
            continue
        if select:
            row = [row[index] for index in indices]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning(f'Row {rowno}: Couldn\'t convert {row}')
                    log.debug(f'Row {rowno}: {e}')
                else:
                    continue
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)
    return records
