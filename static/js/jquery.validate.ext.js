


//日期类型 2012-12-12
jQuery.validator.methods.date = function (value, element) {
	return this.optional(element) || (/^\d{4}-(?:0\d|1[0-2])-(?:[0-2]\d|3[01])$/.test(value));
}

//时间类型验证 11:11:11
jQuery.validator.addMethod("time", function (value, element) {
	return this.optional(element) || /^([01]\d|2[0-3])(:[0-5]\d){1,2}$/.test(value);
}, "请输入一个有效的时间");

//日期时间类型验证 2012-12-12 11:11:11
jQuery.validator.addMethod("dateTime", function (value, element) {
	return this.optional(element) || /^\d{4}-(?:0\d|1[0-2])-(?:[0-2]\d|3[01])( (?:[01]\d|2[0-3])\:[0-5]\d\:[0-5]\d)?$/.test(value);
}, "请输入一个有效的日期时间");

//中国手机号码验证       
jQuery.validator.addMethod("mobile", function (value, element) {
	var length = value.length;
	var mobile = /^(((13[0-9]{1})|(15[0-9]{1}))+\d{8})$/;
	return this.optional(element) || (length == 11 && mobile.test(value));
}, "请输入一个有效的手机号码");

//字节长度验证，汉字（非ASCII字符）按照两个字节长度计算
jQuery.validator.addMethod("rangeBytes", function (value, element, params) {
	var length = value.length;
	for (var i = 0; i < value.length; i++) {
		if (value.charCodeAt(i) > 127) {
			length++;
		}
	}
	return this.optional(element) || (length >= params[0] && length <= params[1]);
}, jQuery.validator.format("请输入 {0} 到 {1} 个字符"));
jQuery.validator.addMethod("maxBytes", function (value, element, param) {
	var length = value.length;
	for (var i = 0; i < value.length; i++) {
		if (value.charCodeAt(i) > 127) {
			length++;
		}
	}
	return this.optional(element) || length <= param;
}, jQuery.validator.format("请输入最多 {0} 个字符"));
jQuery.validator.addMethod("minBytes", function (value, element, param) {
	var length = value.length;
	for (var i = 0; i < value.length; i++) {
		if (value.charCodeAt(i) > 127) {
			length++;
		}
	}
	return this.optional(element) || length >= param;
}, jQuery.validator.format("请输入最少 {0} 个字符")); 