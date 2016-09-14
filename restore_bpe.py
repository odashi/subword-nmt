#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Yusuke Oda


import sys
import argparse


def create_parser():
  parser = argparse.ArgumentParser(description="restore BPE subwords")

  parser.add_argument(
    '--input', '-i', type=argparse.FileType('r'), default=sys.stdin,
    metavar='PATH',
    help="Input file (default: standard input).")
  parser.add_argument(
    '--output', '-o', type=argparse.FileType('w'), default=sys.stdout,
    metavar='PATH',
    help="Output file (default: standard output)")

  return parser


def main():
  parser = create_parser()
  args = parse_args()


if __name__ == '__main__':
  parser = create_parser()
  args = parser.parse_args()

  EOW = '</w>'

  for line in args.input:
    result = ''
    for word in line.split():
      if word.endswith(EOW):
        word = word[:-len(EOW)] + ' '
      result += word
    args.output.write(result.strip())
    args.output.write('\n')
