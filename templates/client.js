const loginForm=document.getElementById('login-form')


if (loginForm){
	loginForm.addEventListener('submit',handleLogin)
}

function handleLogin(event){
	event.preventDefault()
	const loginEndpoint='http://localhost:8000/api/token/'
	let loginFormData=new FormData(loginForm)
	let loginObjectData=Object.fromEntries(loginFormData)
	let bodyStr=JSON.stringify(loginObjectData)
	const options={
		method:"POST",
		headers:{
			"content-type":"application/json"
		},
		body:bodyStr
	}
	fetch(loginEndpoint,options) //promise
	.then(response=>{
		//console.log(response)
		return response.json()
	}).then(x=>{
		console.log(x)
	}).catch(err=>{
		console.log(err)
	})
}