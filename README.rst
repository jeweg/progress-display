progress-display
================

A very simple Python port of `boost::progress_display`_.
It's a console-based progress bar which will strictly append output and
hence doesn't require any cursor positioning terminal capabilities.

.. _boost::progress_display: http://www.boost.org/doc/libs/1_49_0/libs/timer/doc/original_timer.html#Class%20progress_display

Example
-------

::

    pb = ProgressBar(100)
    for _ in xrange(50):
        pb.step()

displays:

::

   0%   10   20   30   40   50   60   70   80   90  100%
   |----|----|----|----|----|----|----|----|----|----|
   **************************
