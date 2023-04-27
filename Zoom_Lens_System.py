#Importing the bpy module for scripting Blender in Python
import bpy 

#The lens system of the Cooke triplet comprises SIX distinct materials:

#Function to add a new material to the scene
def newMaterial(id): 

    mat = bpy.data.materials.get(id)

    if mat is None:
        mat = bpy.data.materials.new(name=id)

    mat.use_nodes = True

    if mat.node_tree:
        mat.node_tree.links.clear()
        mat.node_tree.nodes.clear()

    return mat

###Function to add a new shader (emission and glass(LAH66)) to the scene
def newShader(id, type, r, g, b):

    mat = newMaterial(id)

    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    output = nodes.new(type='ShaderNodeOutputMaterial')

    if type == "emission":
        shader = nodes.new(type='ShaderNodeEmission')
        nodes["Emission"].inputs[0].default_value = (r, g, b, 1)
        nodes["Emission"].inputs[1].default_value = 4

    elif type == "glass":
        shader = nodes.new(type='ShaderNodeBsdfGlass')
        nodes["Glass BSDF"].inputs[0].default_value = (r, g, b, 1)
        nodes["Glass BSDF"].inputs[1].default_value = 0
        nodes["Glass BSDF"].inputs[2].default_value = 1.7725
        
    links.new(shader.outputs[0], output.inputs[0])

    return mat

#Function to create and add a new object to the scene
def drawObject():
    
    #We can add multiple objects to the system, also we can model the object(Candle, car, football etc.) in blender itself instead of just using addons from blender
    ##Adding 3D Objects to the scene from Blender addon
    mat = newShader("Shader1", "emission", 1, 0.021157, 0.0444519)
    bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', 
    location=(91.15, 0, 0), rotation=(-0.190241, 1.01055, 1.78024), scale=(1, 1, 1))
    bpy.context.active_object.data.materials.append(mat)

    mat = newShader("Shader2", "emission", 0.00823272, 0.0161299, 1)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, 
    align='WORLD', location=(91.15,4.7,0), scale=(0.5,0.5,0.5))
    bpy.context.active_object.data.materials.append(mat)
    
    ##Adding Lens system to the scene
    #Lens 1
    mat = newShader("LAH66", "glass", 1,1,1)
    bpy.ops.mesh.add_lens(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0), 
    rad1=-16.202, rad2=-48.876, lensradius=2.952, centerthickness=5.18, flen_intern=-51.1766, flen=-51.1766)
    bpy.context.active_object.data.materials.append(mat)
    
    #Lens 8
    mat = newShader("LAH66", "glass", 1,1,1)
    bpy.ops.mesh.add_lens(align='WORLD', location=(-37.47, 0, 0), rotation=(0, 0, 0), 
    rad1=-10.5831, rad2=-44.4444, lensradius=4.42278, centerthickness=1.22, material_name="LAH66", flen_intern=-28.1192, flen=-28.1192)
    bpy.context.active_object.data.materials.append(mat)
    
   
drawObject()

###Function to add a new glass shader(LLF6) to the scene
def newShader(id, type, r, g, b):

    mat = newMaterial(id)

    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    output = nodes.new(type='ShaderNodeOutputMaterial')

  
    if type == "glass":
        shader = nodes.new(type='ShaderNodeBsdfGlass')
        nodes["Glass BSDF"].inputs[0].default_value = (r, g, b, 1)
        nodes["Glass BSDF"].inputs[1].default_value = 0
        nodes["Glass BSDF"].inputs[2].default_value = 1.5317

    links.new(shader.outputs[0], output.inputs[0])

    return mat

def drawObject():
    
    #Lens 2
    mat = newShader("LLF6", "glass", 1,1,1)
    bpy.ops.mesh.add_lens(align='WORLD', location=(-5.28, 0, 0), rotation=(0, 0, 0), 
    ltype2='aspheric', rad1=15.665, rad2=-42.955, lensradius=4.077, centerthickness=4.4, flen_intern=23.5468, flen=23.5468)
    bpy.context.active_object.data.materials.append(mat)
    
   
drawObject() 

###Function to add a new glass shader(TIH6) to the scene
def newShader(id, type, r, g, b):

    mat = newMaterial(id)

    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    output = nodes.new(type='ShaderNodeOutputMaterial')

    if type == "glass":
        shader = nodes.new(type='ShaderNodeBsdfGlass')
        nodes["Glass BSDF"].inputs[0].default_value = (r, g, b, 1)
        nodes["Glass BSDF"].inputs[1].default_value = 0
        nodes["Glass BSDF"].inputs[2].default_value = 1.8052
        
        
   
    links.new(shader.outputs[0], output.inputs[0])

    return mat

def drawObject():
    
    #Lens 3
    mat = newShader("TIH6", "glass", 1,1,1)
    bpy.ops.mesh.add_lens(align='WORLD', location=(-9.84, 0, 0), rotation=(0, 0, 0), 
    rad1=108.696, rad2=23.624, lensradius=4.399, centerthickness=1, flen_intern=-60.606, flen=-60.606)
    bpy.context.active_object.data.materials.append(mat)
    
   
drawObject()   
        
###Function to add a new glass shader(FSL5) to the scene
def newShader(id, type, r, g, b):

    mat = newMaterial(id)

    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    output = nodes.new(type='ShaderNodeOutputMaterial')

    if type == "glass":
        shader = nodes.new(type='ShaderNodeBsdfGlass')
        nodes["Glass BSDF"].inputs[0].default_value = (r, g, b, 1)
        nodes["Glass BSDF"].inputs[1].default_value = 0
        nodes["Glass BSDF"].inputs[2].default_value = 1.4875
    
    links.new(shader.outputs[0], output.inputs[0])

    return mat

def drawObject():
    
    #Lens 4
    mat = newShader("FSL5", "glass", 1,1,1)
    bpy.ops.mesh.add_lens(align='WORLD', location=(-10.84, 0, 0), rotation=(0, 0, 0), 
    ltype2='aspheric', rad1=23.624, rad2=-16.059, lensradius=4.437, centerthickness=4.96, material_name="FSL5", flen_intern=19.9517, flen=19.9517)
    bpy.context.active_object.data.materials.append(mat)
    
    
    #Lens 5
    mat = newShader("FSL5", "glass", 1,1,1)
    bpy.ops.mesh.add_lens(align='WORLD', location=(-25.28, 0, 0), rotation=(0, 0, 0), 
    ltype1='aspheric', ltype2='spherical', rad1=-425.532, rad2=-35.436, lensradius=4.452, centerthickness=4.04, flen_intern=77.044, flen=77.044)
    bpy.context.active_object.data.materials.append(mat)
    
   
drawObject() 

###Function to add a new glass shader(LAL8) to the scene
def newShader(id, type, r, g, b):

    mat = newMaterial(id)

    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    output = nodes.new(type='ShaderNodeOutputMaterial')

    if type == "glass":
        shader = nodes.new(type='ShaderNodeBsdfGlass')
        nodes["Glass BSDF"].inputs[0].default_value = (r, g, b, 1)
        nodes["Glass BSDF"].inputs[1].default_value = 0
        nodes["Glass BSDF"].inputs[2].default_value = 1.7310
   
    links.new(shader.outputs[0], output.inputs[0])

    return mat

def drawObject():
    
    #Lens 6
    mat = newShader("LAL8", "glass", 1,1,1)
    bpy.ops.mesh.add_lens(align='WORLD', location=(-30.67, 0, 0), rotation=(0, 0, 0), 
    rad1=-14.146, rad2=-251.256, lensradius=4.237, centerthickness=1, flen_intern=-30.0221, flen=-30.0221)
    bpy.context.active_object.data.materials.append(mat)
    
   
drawObject()    
              
###Function to add a new glass shader(PBH25) to the scene
def newShader(id, type, r, g, b):

    mat = newMaterial(id)

    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    output = nodes.new(type='ShaderNodeOutputMaterial')

    if type == "glass":
        shader = nodes.new(type='ShaderNodeBsdfGlass')
        nodes["Glass BSDF"].inputs[0].default_value = (r, g, b, 1)
        nodes["Glass BSDF"].inputs[1].default_value = 0
        nodes["Glass BSDF"].inputs[2].default_value = 1.7618
     
    links.new(shader.outputs[0], output.inputs[0])

    return mat

def drawObject():
    
    #Lens 7
    mat = newShader("PBH25", "glass", 1,1,1)
    bpy.ops.mesh.add_lens(align='WORLD', location=(-31.67, 0, 0), rotation=(0, 0, 0), 
    rad1=-251.256, rad2=-22.502, lensradius=4.348, centerthickness=2.8, flen_intern=49.2301, flen=49.2301)
    
    bpy.context.active_object.data.materials.append(mat)
    
   
drawObject()     
   
#Add Detector to the lens system
bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', 
location=(-55, 0, 0), rotation=(1.57, 0, 4.71), scale=(3,3,3))
bpy.context.object.data.lens = 4.3
bpy.context.object.data.sensor_width = 8.4
bpy.context.scene.render.resolution_x = 1280
bpy.context.scene.render.resolution_y = 1900

#Enable certain features of Eevee rendering engine
bpy.context.scene.eevee.use_gtao = True
bpy.context.scene.eevee.use_ssr = True
bpy.context.scene.eevee.use_ssr_refraction = True
bpy.context.object.mat2.use_screen_refraction = True

