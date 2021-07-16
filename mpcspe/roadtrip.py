# -*- coding: utf-8 -*-
"""
Created on Friday, 16th July 2021 9:59:45 am
===============================================================================
@filename:  roadtrip2.py
@author:    Manuel Martinez (manmart@uchicago.edu)
@project:   mpcspe | 2018-19
@purpose:   Road Trip!
===============================================================================
"""
import sys
from typing import Dict, List


class City:
    def __init__(self, s: str, t: int) -> None:
        self.s: str = s
        self.t: int = t
        self.v: int = -1


class Trip:
    def __init__(self, n: int, r: int, s: int, m: int, h: int) -> None:
        self.n = n
        self.r = r
        self.s = s
        self.m = m
        self.h = h
        self.t = 0
        self.cities: List[City] = []
        self.roads: Dict[tuple, int] = {}
        self.path: List[City] = []

    def add_city(self, city: City) -> None:
        self.cities.append(city)

    def add_road(self, origin: int, destination: int, d: int) -> None:
        self.roads[(origin, destination)] = d
        self.roads[(destination, origin)] = d

    def get_path(self) -> List[str]:
        return [city.s for city in self.path]

    def traverse(self) -> None:
        current = self.s
        next_city = self.s
        n_visited: int = 0

        while True:
            if n_visited != 0:
                next_city = self._get_next_city(current)
                if next_city == -1:
                    break
                else:
                    self.t += self.roads[current, next_city]
            else:
                pass

            self.t += self.cities[next_city].t
            self.cities[next_city].v = self.t
            self.path.append(self.cities[next_city])

            current = next_city
            n_visited += 1

    def _get_next_city(self, origin: int) -> int:
        # get roads from origin
        possibles = [k for k, _ in self.roads.items() if origin == k[0]]
        filtered = []
        for possible in possibles:
            d = self.roads[possible]
            if (self.t + d - self.cities[possible[1]].v) < self.h:
                if self.cities[possible[1]].v == -1:
                    filtered.append(possible)
                else:
                    continue
            if (self.t + d + self.cities[possible[1]].t) > self.m:
                continue
            filtered.append(possible)

        if len(filtered) == 0:
            return -1
        if len(filtered) == 1:
            return filtered[0][1]
        else:
            ds = [self.roads[possible] for possible in filtered]
            result = filtered[ds.index(min(ds))]
            return result[1]


def main(line: str) -> None:
    lines = line.splitlines()
    n, r, h, m, s = map(int, lines[0].split())
    trip = Trip(n=n, r=r, s=s, m=m, h=h)
    for i in range(1, n + 1):
        _, cs, ct = lines[i].split()
        city = City(s=cs, t=int(ct))
        trip.add_city(city)
    for i in range(n + 1, n + r + 1):
        orig, dest, d = map(int, lines[i].split())
        trip.add_road(origin=orig, destination=dest, d=d)
    trip.traverse()
    sys.stdout.write(' '.join(trip.get_path()))
    sys.stdout.write('\n')
    sys.stdout.write(str(trip.t))


if __name__ == "__main__":
    main(sys.stdin.read())
