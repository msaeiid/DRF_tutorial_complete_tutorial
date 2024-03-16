const loginForm=document.getElementById('login-form')
const contentContainer=document.getElementById('content-container')
const searchForm=document.getElementById('search-form')
const baseEndpoint='http://localhost:8000'


if (loginForm){
	loginForm.addEventListener('submit',handleLogin)
}

if (searchForm){
	searchForm.addEventListener('submit',handleSearch)
}

function handleLogin(event){
	event.preventDefault()
	const loginEndpoint= `${baseEndpoint}/api/token/`
	let loginFormData=new FormData(loginForm)
	let loginObjectData=Object.fromEntries(loginFormData)
	const options=getFetchOptions("POST",loginObjectData)
	fetch(loginEndpoint,options) //promise
	.then(response=>{
		return response.json()
	}).then(authData=>{

		handleAuthentication(authData,getProductList)
		})
	.catch(err=>{
		alert(err)
	})
}
// saving such critical data in local storage is not a good idea
function handleAuthentication(authData,callback){
	localStorage.setItem('access',authData.access)
	localStorage.setItem('resfresh',authData.refresh)
	callback()
}


function writeToContent(data){
	if (contentContainer){
		contentContainer.innerHTML="<pre>"+JSON.stringify(data,null,4)+"</pre>"
	}
}

function getFetchOptions(method,jsObject){
	return {
		method: method == null ? "GET" :method,
		headers:{
			"content-type":"application/json",
			"Authorization":`Bearer ${localStorage.getItem('access')}`
		},
		body:jsObject ? JSON.stringify(jsObject):null
	}
}

function getProductList(){
	const endpoint=`${baseEndpoint}/product/`
	const options=getFetchOptions()
	fetch(endpoint,options)
	.then(response=>{
		return response.json()
		})
	.then(data=>{
		const validData=isTokenNotValid(data)
		if (validData){
			writeToContent(data)	
		}
	})
}

function isTokenNotValid(jsonData){
	if ( jsonData.code == "token_not_valid"){
		
		//refresh token
		alert("Please login again")
		return false
	}
	return true
}



function validateJWTToken(){
	const endpoint = `${baseEndpoint}/api/token/verify/`
	const token=localStorage.getItem("access")
	if (token){
			const options={
				method: "POST",
				headers:{
					"content-type":"application/json"
					},
					body:JSON.stringify({
						token:localStorage.getItem('access')}
					)}			
					console.log(endpoint)
			fetch(endpoint,options)
			.then(response=>response.json())
			.then(x=>{
				//refresh token...
				console.log(x)
				isTokenNotValid(x)
				})
	}
	else{
		console.log("access token not found!")
}
}
validateJWTToken()


function handleSearch(event){
	event.preventDefault()
	let formData=new FormData(searchForm)
	let data=Object.fromEntries(formData)
	let searchParams=new URLSearchParams(data)
	const endpoint=`${baseEndpoint}/product/search?${searchParams}`
	const headers={
		"content-type":"application/json"
	}
	const authToken = localStorage.getItem('access')
	if (authToken){
		headers['Authorization']=`Bearer ${authToken}`
	}
	const options={
		method: "GET",
		headers:headers
	}
	fetch(endpoint,options)
	.then(response=>{
		return response.json()
	})
	.then(data=>{
		console.log(data.hits)
		writeToContent(data)
		})
	.catch(err=>{console.log(err)})
}