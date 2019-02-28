from lora.parse import get_args
from lora.utils import print_params, sim

def main(args):
    # import agruments
    nrNodes = int(args.nrNodes)
    nrIntNodes = int(args.nrIntNodes)
    nrBS = int(args.nrBS)
    radius = int(args.radius)
    avgSendTime = int(args.AvgSendTime)
    horTime = int(args.horizonTime)
    packetLength = int(args.packetLength)
    sfSet = list(map(int, args.sfSet.split()))
    freqSet = list(map(int, args.freqSet.split()))
    powSet = list(map(int, args.powerSet.split()))
    captureEffect = bool(args.captureEffect)
    interSFInterference = bool(args.interSFInterference)
    info_mode = str(args.infoMode)
    exp_name = str(args.exp_name)
    logdir = str(args.logdir)
    
    # print simulation parameters
    print("\n=================================================")
    print_params(nrNodes, nrIntNodes, nrBS, radius, avgSendTime, horTime, packetLength, 
                sfSet, freqSet, powSet, captureEffect, interSFInterference, info_mode)

    # running simulation
    bsDict, nodeDict = sim(nrNodes, nrIntNodes, nrBS, radius, avgSendTime, horTime, packetLength, 
    sfSet, freqSet, powSet, captureEffect, interSFInterference, info_mode, logdir, exp_name)

    return bsDict, nodeDict

if __name__ == '__main__':
    # import agruments
    args = get_args()
    # print args and run simulation
    bsDict, nodeDict = main(args)