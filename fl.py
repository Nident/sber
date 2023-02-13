# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:16:29 2023

@author: java_school
"""

import time
from pypipeline.components.source.Timer import Timer
from pypipeline.core.DslPipelineBuilder import DslPipelineBuilder
from pypipeline.core.Plumber import Plumber


class Filter:
    def __call__(self, exchange):
        parts = exchange.in_msg.body.split()
        return int(parts[-1]) % 2 == 0
    def main():
        plumber = Plumber()
        builder1 = DslPipelineBuilder()
 
        pipeline1 = builder1 \
        .source(Timer, {"period": 1.0}) \
        .filter(Filter()) \
        .process(lambda ex: print(ex.in_msg.body))
        plumber.add_pipeline(pipeline1)
        plumber.start()
        time.sleep(10)
        plumber.stop()
        
    def filter_method(exchange):
        parts = exchange.in_msg.body.split()
        return int(parts[-1]) % 2 == 0

if __name__ == "__main__":
    main()
    
    