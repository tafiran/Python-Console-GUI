	
<hr name="start" />

<!-- name of project -->
<h3 align="center">
 <b>⚙ Python Console GUI ⚙</b>
</h3>

<!-- introduction  -->
<hr name="i1" />

<img src="https://github.com/tafiran/Python-Console-GUI/blob/main/media/block.png" alt="illustration 1"></img>

<!-- socials -->
<div class="vk" width="50" height="30" color="red">

</div>

<div class="facebook">

</div>

<div class="instagram">

</div>

	
<!-- first block paragraph -->
<div align="center" text-align="justify"> 
If you tried to do console program on Python more intuitive to user, but all these tries led to using some libraries with primitive console menu or tkinter wich looks like a parody of the real app. Can be used web-interface but there are some problems. 
</div> <br />

<!-- reasons why do i create this lib -->
<table align="center">
	<tbody>
	  <tr>
				<td colspan="2" align="center">Reasons</td>
			</tr>
			<tr>
				<td align="center">Not every user is acquaintanted to web tecnologies.</td>
			</tr>
			<tr>
				<td align="center">If the program that you do is primitive, there is no reason to use web.</td>
			</tr>
		</tbody>
</table> <br />
<p align="center">This is why I decided to create this library. Python console GUI has a simple interface to maintain visual contact with the user.</p><br />

<!-- features of library -->
<table align="center">
	<tbody>
  <tr>
			<td colspan="2" align="center">Features</td>
		</tr>
		<tr>
			<td>Block System</td>
			<td>Possibility to add blocks and set them as you want</td>
		</tr>
		<tr>
			<td>Css Based</td>
			<td>Configure your blocks and elements as you want with flex-box properties from css</td>
		</tr>
		<tr>
			<td>Types Of Items</td>
			<td>Set items in blocks as you want and cofigure them</td>
		</tr>
	</tbody>
</table> <br />

	
<hr name="content" />

<!-- Content of documentation -->
<h3 align="center" style="font-size: 80px;" id="#content">
 📜 Content of docmentation 📜
<h3> 
	
	
<hr />
	
<!-- content -->
<blockquote align><p><a href="#start">Start of documentation</a></p>
	<blockquote><p><a href="#i1">Introduction</a></p></blockquote>
</blockquote>
	
<blockquote><p><a href="#content">Content</a></p></blockquote>
<blockquote><p><a href="#install">Installation</a></p></blockquote>
<blockquote><p><a href="#examples">Examples</a></p>
	<blockquote><p><a href="#e1">Using of library</a></p></blockquote>
</blockquote>
	
<hr name="install" />

<!-- title -->
<h3 align="center">
 <b>🧭 Installation 🧭</b>
</h3>

<!-- installation  -->
<hr />
	
	    $ pip3 install vk_api

<hr name="examples"/>
	
<!-- title -->
<h3 align="center">
 <b>🖋 Examples 🖋</b>
</h3>

<!-- examples  -->
	
<hr />
	
<h4 name="e1" align="center">An example of using this library</h4>
	
```Python
from consoleGUI import *

# creating menu object
exampleMenu = menuObject()

# first block
firstBlock = block()
firstBlock.addItem()

# second block
secondBlock = block()
secondBlock.addItem()

# main block
main = block()
main.addBlock()
main.addItem()

main.display()
```
	
<hr name="struct"/>
	
<!-- title -->
<h3 align="center">
 <b>✅ Structure ✅</b>
</h3>

<!-- examples  -->
	
<hr />
