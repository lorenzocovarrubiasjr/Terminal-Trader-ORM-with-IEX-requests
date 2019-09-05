#! /usr/bin/env python3

from data import schema, seed 

if __name__ == "__main__":
    schema.schema()
    seed.seed()
