function stringify(x) {
	wrap = (x => "\"" + x + "\"");
	switch(toString.call(x)) {
		case "[object Boolean]":
		case "[object Number]":
			return x.toString();
		case "[object String]":
			return wrap(x);
		case "[object Array]":
			return "[" + ( x.map(x => stringify(x)) ).join(',') + "]";
		case "[object Object]":
			result = [];
			for(let key in x) {
				if (stringify(x[key]) !== undefined) {
					result.push(wrap(key) + ":" + stringify(x[key]));
				}
			}
			return "{" + result.join(',') + "}";
		default:
			return undefined;
	}
}