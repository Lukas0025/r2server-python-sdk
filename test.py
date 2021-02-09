import r2server.api
import r2server.tools.common

# init api
network = r2server.api()

# get last observations by METEOR M2
obs = network.observation(33591)

# print all filtred observations ids
for ob in obs:
    if ob.haveA:
        image = ob.a()
        r2server.tools.common.bin2file(image, "img/" + str(ob.id) + ".jpg")