#Importing the bpy module for scripting Blender in Python
import bpy 

##To incorporate SK16 and F2 materials into the Cooke Triplet lens system, we must create a function that adds each material to the scene twice.

#Function to add a new material_1 to the scene
def newMaterial(id): 
    
    mat = bpy.data.materials.get(id)

    if mat is None:
        mat = bpy.data.materials.new(name=id)

    mat.use_nodes = True

    if mat.node_tree:
        mat.node_tree.links.clear()
        mat.node_tree.nodes.clear()

    return mat

def newShader(id, type, r, g, b):

    mat = newMaterial(id)

    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    output = nodes.new(type='ShaderNodeOutputMaterial')

    if  type == "emission":
        shader = nodes.new(type='ShaderNodeEmission')
        nodes["Emission"].inputs[0].default_value = (r, g, b, 1)
        nodes["Emission"].inputs[1].default_value = 4
        
    elif type == "glass":
        shader = nodes.new(type='ShaderNodeBsdfGlass')
        nodes["Glass BSDF"].inputs[0].default_value = (r, g, b, 1)
        nodes["Glass BSDF"].inputs[1].default_value = 0
        nodes["Glass BSDF"].inputs[2].default_value = 1.61824

    links.new(shader.outputs[0], output.inputs[0])
    
    return mat


#Function to create and add a new object to the scene
def drawObject():
    
    #Adding 3D Object to the scene from Blender addon
    mat = newShader("Shader1", "emission", 1, 0.021157, 0.0444519)
    bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', 
    location=(31.157, 0, 0), rotation=(-0.190241, 1.01055, 1.78024), scale=(1, 1, 1))
    bpy.context.active_object.data.materials.append(mat)
      
 
    ##Adding Lens system to the scene
    #Lens 1
    mat = newShader("SK16", "glass", 1,1,1)
    bpy.ops.mesh.add_lens(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0), 
    rad1=22.014, rad2=-435.76, lensradius=9.5, centerthickness=3.259, flen_intern=42.0104, flen=42.0104)
    bpy.context.active_object.data.materials.append(mat)
    #bpy.context.object.use_screen_refraction = True
    
   
    #Lens3
    mat = newShader("SK16", "glass", 1,1,1)
    bpy.ops.mesh.add_lens(align='WORLD', location=(-15.017, 0, 0), rotation=(0, 0, 0), rad1=79.684, 
    rad2=-18.395, lensradius=7.5, centerthickness=2.952, flen_intern=30.1928, flen=30.1928)
    bpy.context.active_object.data.materials.append(mat)
    #bpy.context.object.use_screen_refraction = True
    
drawObject()


#Function to add a new material_2 to the scene
def newMaterial(id):

    mat = bpy.data.materials.get(id)

    if mat is None:
        mat = bpy.data.materials.new(name=id)

    mat.use_nodes = True

    if mat.node_tree:
        mat.node_tree.links.clear()
        mat.node_tree.nodes.clear()

    return mat

def newShader(id, type, r, g, b):

    mat = newMaterial(id)

    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    output = nodes.new(type='ShaderNodeOutputMaterial')

    if type == "glass":
        shader = nodes.new(type='ShaderNodeBsdfGlass')
        nodes["Glass BSDF"].inputs[0].default_value = (r, g, b, 1)
        nodes["Glass BSDF"].inputs[1].default_value = 0
        nodes["Glass BSDF"].inputs[2].default_value = 1.61656
    
    
    links.new(shader.outputs[0], output.inputs[0])

    return mat


def drawObject():

#Lens2        
 mat = newShader("F7", "glass", 1,1,1)
 bpy.ops.mesh.add_lens(align='WORLD', location=(-9.267, 0, 0), rotation=(0, 0, 0), rad1=-22.213, 
 rad2=20.292, lensradius=5, centerthickness=1, flen_intern=-21.0441, flen=-21.0441)
 bpy.context.active_object.data.materials.append(mat)    
 bpy.context.object.use_screen_refraction = True

drawObject()



#Add Detector to the lens system
bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', 
location=(-35.1446, 0, 0), rotation=(1.57, 0, 4.71), scale=(3,3,3))
bpy.context.object.data.lens = 4.3
bpy.context.object.data.sensor_width = 8.4
bpy.context.scene.render.resolution_x = 1280
bpy.context.scene.render.resolution_y = 1900

#Enable certain features of Eevee rendering engine
bpy.context.scene.eevee.use_gtao = True
bpy.context.scene.eevee.use_ssr = True
bpy.context.scene.eevee.use_ssr_refraction = True
bpy.context.object.mat2.use_screen_refraction = True
