data = {}
is_recording = False
with open("data.txt") as data_file:
    for row in data_file:
        row = unicode(row.strip(), encoding = 'utf-8')
        if "CountRateArray =" in row:
            is_recording = True
            continue
        elif "CorrelationArraySize =" in row:
            is_recording = False
            continue
        if is_recording:
            time, intensity = [int(float(i)) for i in row.split()]

#populate data {} with keys ( times) and values ( intensities)  
            if data.has_key(time):            
                data[time].append(intensity)
            else:
                data[time] = [intensity]

# the dictionary is  filled   

# save as csv. 'w' allows us to write on it
with open("output.csv", "w") as out_file:
    for k, v in sorted(data.items()):
# join data values (intensity ) into strings for output
        a = ', '.join(str(x) for x in v)
        out_file.write("%d, %s\n" % (k, a))
