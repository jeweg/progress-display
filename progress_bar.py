#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import with_statement

import sys

class ProgressBar(object):
    """"A console-based progress bar display.
    This is pretty much a straight port of boost::progress_display."""

    def __init__(self, num_steps, output_file=None,
                 string1='',
                 string2='',
                 string3=''):
        self.output_file = sys.stdout if output_file is None else output_file
        self.num_steps = num_steps
        self.string1 = string1
        self.string2 = string2
        self.string3 = string3
        self.steps_taken = 0
        self._tics_drawn = 0
        self.restart()


    def restart(self):
        """Restarts the display, printing the scale again and starting with an
        empty bar."""
        self.steps_taken = 0
        self._tics_drawn = 0
        self.output_file.write(self.string1 + \
            '0%   10   20   30   40   50   60   70   80   90  100%\n' + \
            self.string2 + \
            '|----|----|----|----|----|----|----|----|----|----|\n')
        self.output_file.flush()
        self.output_file.write(self.string3)


    def step(self, steps=1):
        """Advances the progress display, possibly printing another tic.

        Args:
            * steps: the number of steps to take. Must be a number > 0 but
                     does not have to be an integer.

        Raises:
            * ValueError: if the steps argument is not > 0.
        """
        def _steps_to_tics(s):
            return int(round(s * 51.0 / self.num_steps))

        if steps <= 0:
            raise ValueError('steps must be > 0')

        # Increase steps taken, but clamp against maximum.
        self.steps_taken += steps
        self.steps_taken = min([self.steps_taken, self.num_steps])

        tics_to_draw = _steps_to_tics(self.steps_taken) - self._tics_drawn
        self.output_file.write('*' * tics_to_draw)
        tics_drawn_before = self._tics_drawn
        self._tics_drawn += tics_to_draw

        # Add the newline once we have written the last tic, but
        # take the clamping into account: it must be written only once.
        if self._tics_drawn == 51 and tics_drawn_before < 51:
            self.output_file.write('\n')

            
if __name__ == '__main__':
    # Demo:

    import time
    pb = ProgressBar(100,
                     string1='\nHello ',
                     string2='World ',
                     string3='      ')

    for i in xrange(100): # 0 to 100 is 100 steps.
        pb.step()
        time.sleep(0.05)
        if i == 50:
            pb.restart()
            break

    for _ in xrange(100):
        pb.step()
        time.sleep(0.05)

    pb = ProgressBar(3)
    time.sleep(1)
    for _ in xrange(3):
        pb.step()
        time.sleep(1)

    pb = ProgressBar(3)
    for _ in xrange(300):
        pb.step(0.01)
        time.sleep(0.01)

    # Overflowing should get ignored:
    for _ in xrange(300):
        pb.step(0.01)
        time.sleep(0.005)

    print 'done.'
