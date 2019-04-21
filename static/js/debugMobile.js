
function DebuggerMobile(debug,url){
    url = url ? url:{}
    this.debug = debug ? debug:true
    this.protocol = url.protocol ? url.protocol : location.protocol
    this.host = url.host ? url.host:document.domain.toString()
    this.port = url.port ? url.port:location.port
    this.namespace = url.namespace ? url.namespace:'/debugger'

    this.socket = null
}

DebuggerMobile.prototype.start = function(){
    if(this.debug !== true){return false}
    var self = this
    var url = this.protocol+'//'+this.host+':'+this.port+this.namespace

    this.socket = io.connect(url)

    window.onerror = function(msg,url,line,column,error){
        self.socket.emit('debugError',{msg:msg.toString(),
                                       error:error.toString(),
                                       url:url,
                                       line:line,
                                       column:column})
        return false
    }

    $(document).ajaxError(function(event,jqxhr,setting,error){
        self.socket.emit('debugAjax',{url:setting.url,error:error,responseText:jqxhr.responseText})
    })
}