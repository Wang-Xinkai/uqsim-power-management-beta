import sys
import os
import json
import make_arch as march 

# compose
def main():
	# req path
	recvTm = march.make_time_model("expo", [55300])
	respTm = None
	proc_stage = march.make_stage(stage_name = "compose_proc", pathId = 0, pathStageId = 0, stageId = 0, blocking = False, batching = False, socket = False, 
		epoll = False, ngx = False,  net = False, chunk = False, recvTm = recvTm, respTm = respTm, cm = None, criSec = False, threadLimit = None, 
		scaleFactor = 0.55, useHist = False)


	recvTm = march.make_time_model("const", [0])
	respTm = None
	thrift_stage = march.make_stage(stage_name = "thrift_proc", pathId = 0, pathStageId = 1, stageId = 1, blocking = False, batching = False, socket = False, 
		epoll = False, ngx = False,  net = True, chunk = False, recvTm = recvTm, respTm = respTm, cm = None, criSec = False, threadLimit = None, 
		scaleFactor = 0.55, useHist = False)

	req_path = march.make_code_path(pathId = 0, prob = 100, stages=[proc_stage, thrift_stage], priority = None)

	# compose
	compose = march.make_micro_service(servType = "micro_service", servName = "compose", bindConn = True, paths = [req_path], 
		baseFreq = 2600, curFreq = 2600)

	with open("./json/microservice/compose.json", "w+") as f:
		json.dump(compose, f, indent=2)


if __name__ == "__main__":
	main();