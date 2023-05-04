import bpy #Importing the bpy module for scripting Blender in Python

def newMaterial(id): #Function to add a new material to the scene

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

    if type == "emission":
        shader = nodes.new(type='ShaderNodeEmission')
        nodes["Emission"].inputs[0].default_value = (r, g, b, 1)
        nodes["Emission"].inputs[1].default_value = 4
        
    elif type == "glass":
        shader = nodes.new(type='ShaderNodeBsdfGlass')
        nodes["Glass BSDF"].inputs[0].default_value = (r, g, b, 1)
        nodes["Glass BSDF"].inputs[1].default_value = 0
        nodes["Glass BSDF"].inputs[2].default_value = 1.517
        
    links.new(shader.outputs[0], output.inputs[0])

    return mat


def drawObject(): #Function to create and add a new object to the scene
   
    #Adding Object to the scene
    mat = newShader("Shader2", "emission", 0.00823272, 0.0161299, 1)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, 
    align='WORLD', location=(31.15,0.7,0), scale=(0.5,0.5,0.5))
    bpy.context.active_object.data.materials.append(mat)
    
    #Adding Lens to the scene
    mat2 = newShader("Bk7", "glass", 1,1,1)
    bpy.ops.mesh.add_lens(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0),
    rad1=9, rad2=-12, lensradius=3, centerthickness=1.5, flen_intern=10.5366, flen=10.5366)

    bpy.context.active_object.data.materials.append(mat2)
    
drawObject()

#Add Detector to the lens system
bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', 
location=(-15.447, 0, 0), rotation=(1.57, 0, 4.71), scale=(1,1,1))
bpy.context.object.data.lens = 4.3
bpy.context.object.data.sensor_width = 8.4
bpy.context.scene.render.resolution_x = 1280
bpy.context.scene.render.resolution_y = 1900

#Enable certain features of Eevee rendering engine
bpy.context.scene.eevee.use_gtao = True
bpy.context.scene.eevee.use_ssr = True
bpy.context.scene.eevee.use_ssr_refraction = True
bpy.context.object.mat2.use_screen_refraction = True

### IMPORTANT!
###Once the above code has been executed, all that is required is to manually enable Screen Space Reflections for each lens by accessing the Material Tab and clicking on the corresponding option.