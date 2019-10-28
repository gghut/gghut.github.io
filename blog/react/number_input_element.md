```html
class PriceInputor extends Component{

    handChange(e){
        if(this.props.onValueChange){
            this.props.onValueChange(e.target.value)
        }
    }

    handInputCheck(e){
        e.target.value=e.target.value.replace(/[^\d]/g,'')
    }

    render(){
        return (<input typtexte="text" onInput={(e)=>this.handInputCheck(e)} placeholder={this.props.placeholder} onChange={(e)=>{this.handChange(e)}}></input>)
    }
}
```