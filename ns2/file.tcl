Class sports


sports instproc worth {} {
	$self instvar value
	puts "very famous not so much value as $value"
}

Class cricket -superclass sports


cricket instproc worth {} {
	$self instvar value
	puts "very famous infact more as value $value"
}


set s [new sports]



$s set value 50
set c [new cricket]
$c set value 100




$s worth
$c worth
