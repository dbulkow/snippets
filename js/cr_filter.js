/*
 * When reading a websocket that contains output from a command
 * line program and it uses carriage returns to overwrite output.
 * Each carriage return needs to push buffer writes back to the
 * last newline.
 *
 * This was written to cope with a program that emits progress
 * bars that look like:
 *
 *    ######---------------------| 20% Writing Firmware
 *
 * Called from a websocket handler similar to this:
 *
 *     var buffer = StringBuffer(),
 *         ws = new WebSocket(url);
 *
 *     ws.onmessage = function(e) {
 *         var out = $("#ws");
 *
 *          var len = e.data.length;
 *          for (i=0; i<len; i++)
 *              buffer.append(e.data[i]);
 *     
 *          out.text(buffer.toString());
 *     }
 */
var StringBuffer = function() {
    var obj = {};

    obj.buffer = [];
    obj.index = 0;
    obj.newline = 0;
    obj.length = 0;

    obj.append = function(ch) {
	if (ch == '\r') {
	    this.index = this.newline;
	    return this;
	};

	if (ch == '\n')
	    this.index = this.length;

	this.buffer[this.index] = ch;
	this.index += 1;

	if (this.index > this.length)
	    this.length = this.index;

	if (ch == '\n')
	    this.newline = this.index;

	return this;
    };

    obj.toString = function() {
	return this.buffer.join('');
    };

    return obj;
};
