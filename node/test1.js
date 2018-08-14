
	var a = 5;
	
	function fn(){
		console.log(a == 5,'fn');
		var a = 1;
		function test(){
			console.log(a == 1,'test');
		}
		test();
	}
	fn();
	// false,'fn'
	// true,'test'