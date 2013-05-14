
  
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>

<head>
<style>
td {
 border: solid 1px black;
}
tr{
 border: solid 1px black;
}
table{
border: solid 1px black;
}
</style>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Update Person Info</title>
</head>


<body>
<div id="home1">
		<jsp:include page="home.jsp"></jsp:include>
	</div>
	
<hr>
<br><br><br><br><br><br><br><br><br><br><br>
<%
Person per= (Person)session.getAttribute("per1");
%>
<h1 align="center" >Video Library Management</h1>

<h2 align="center" >Update Person Info</h2>
<div align="center">
<form name="form1" method="post"  action="UpdatePerson" onSubmit="">


<input type="hidden" name="memid" value="<%=per.getMemberid()%>">


<table border="1">
<tr>
<th>
Account Information
</th>
</tr>

<tr>
<th><div class="form-row"><span class="label">  First Name*</span></th><td><input type="text" name="fname" value="<%=per.getFirstname()%>"/> </div></td>
</tr>

<tr>
<th><div class="form-row"><span class="label">  Last Name*</span></th><td><input type="text" name="lname" value="<%=per.getLastname()%>"/></div></td>
</tr>


<tr>
<th>
Home Address
</th>
</tr>

<tr>
<th><div class="form-row"><span class="label">  Address*</span></th><td><input type="text" name="address" value="<%=per.getAddress()%>"/> </div></td>
</tr>


<tr>
<th><div class="form-row"><span class="label">  City*</span></th><td><input type="text" name="city" value="<%=per.getCity()%>"/> </div></td>
</tr>



<tr>
<th><div class="form-row"><span class="label">  State*</span></th><td><input type="text" name="state" value="<%=per.getState()%>"/> </div></td>
</tr>


<tr>
<th><div class="form-row"><span class="label">  ZipCode*</span></th><td><input type="text" name="zipcode" value="<%=per.getZipcode()%>"/> </div></td>
</tr>


<tr>
<th><div class="form-row"><span class="label">  Country*</span></th><td><input type="text" name="country" value="<%=per.getCountry()%>"/> </div></td>
</tr>



<tr>
<th><div class="form-row"><input class="submit"  type="submit" value="Save Changes"/> </div></th>

<th><div class="form-row"><input class="reset"   type="reset" value="Reset"/> </div></th>
</tr>

</table>

</div>


</form>
</body>
</html>
