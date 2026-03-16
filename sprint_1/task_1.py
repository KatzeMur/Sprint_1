time_str = '1h 45m,360s,25m,30m 120s,2h 60s'

all_minutes = 0

time_period = time_str.split(',')

for p in time_period:
    p = p.replace('h', 'h, ')
    p = p.replace('m', 'm, ')
        
    conversions = p.split(',')
    
    for i in conversions:
        if 'h' in i:
            hours = int(i.replace('h', ''))
            all_minutes += hours * 60
        elif 'm' in i:
            minutes = int(i.replace('m', ''))
            all_minutes += minutes
        elif 's' in i:
            seconds = int(i.replace('s', ''))
            all_minutes += seconds // 60

print(all_minutes)
            
    
    
    
    




