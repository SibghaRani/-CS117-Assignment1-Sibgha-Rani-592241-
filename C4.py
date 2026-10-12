#Compute both unloaded voltage and loaded voltage with a parallel load
def loaded_divider(vs,r1,r2,rl):
    v_unloaded = vs*(r2/(r1+r2))
    r2_parallel_rl = (r2*r1)/(r1+rl)
    v_loaded = vs*(r2_parallel_rl/(r1+r2_parallel_rl))
    return (v_unloaded,v_loaded)
result = loaded_divider(12,1000,1000,500)
print("LOADED DIVIDER(12,1000,1000,500):",result)
