#create a simulator object 

set ns [new Simulator]



#create a trace file,this file is for logging purpose
set tracefile [open wired.tr w]

#f = open(wiredd.tr,w)

$ns trace-all $tracefile



#create a animation information or nam file creation

set namfile [open wired.nam w]
$ns namtrace-all $namfile

#create nodes 

for {set i 0} {$i<6} {incr i} {
	set n($i) [$ns node]
}


set links {{$n(0) $n(1) 5Mb 2ms DropTail} {$n(2) $n(1) 10Mb 5ms DropTail} {$n(1) $n(4) 3Mb 10ms DropTail} {$n(4) $n(3) 100Mb 2ms DropTail} {$n(4) $n(5) 4Mb 10ms DropTail}}
foreach link $links {
eval $ns duplex-link $link
}






#creation of agents
#node 0 to node3
set udp [new Agent/UDP]
set null [new Agent/Null]
$ns attach-agent $n(0) $udp
$ns attach-agent $n(3) $null
$ns connect $udp $null

#creation of another agents
set tcp [new Agent/TCP]
set sink [new Agent/TCPSink]
$ns attach-agent $n(2) $tcp
$ns attach-agent $n(5) $sink
$ns connect $tcp $sink

#creation of Application CBR,FTP
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
set ftp [new Application/FTP]
$ftp attach-agent $tcp

#Start the traffic
$ns at 1.0 "$cbr start"
$ns at 2.0 "$ftp start"

$ns at 10.0 "finish"

proc finish {} {
	global ns tracefile namfile
	$ns flush-trace
	close $tracefile
	close $namfile
	exec nam wired.nam
	exit 0
}
puts "Simulation is starting"

$ns run
