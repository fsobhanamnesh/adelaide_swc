# Run and report 
import dnaContent
from dnaContent import nucleotideContent 
tests=[
	['gtcagtc', {'G':2, 'T':2, 'C':2, 'A':2},],
	['ACTGHR', {}],
    	['gtagt', {'G':2, 'T':2, 'C':0, 'A':2}] 
      ]	
passes = 0    
for (i, (seq, expected)) in enumerate(tests):    
if nucleotideContent(seq) == expected:    
	passes += 1    
else:    
	print('test %d failed' % i)    
    
print('%d/%d tests passed' % (passes, len(test)))

