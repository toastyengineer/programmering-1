'''Profilerar modulen fakultet'''
import cProfile
import pstats
import fakultet
import dice_multi_compare
cProfile.run('dice_multi_compare', 'restats')
p = pstats.Stats('restats')
p.sort_stats('cumulative').print_stats(20)
