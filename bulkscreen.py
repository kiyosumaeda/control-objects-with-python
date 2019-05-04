import bpy

animation_array2 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					[0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],
					[0,0,0,1,2,2,2,2,2,1,1,1,1,0,0,0],
					[0,0,1,2,3,3,2,3,2,2,1,1,1,1,0,0],
					[0,1,2,3,4,4,3,4,3,2,2,1,1,1,1,0],
					[0,1,2,3,4,5,4,4,4,3,3,2,2,1,1,0],
					[0,1,2,3,4,5,5,5,4,3,2,2,2,1,1,0],
					[0,1,2,3,4,4,5,6,5,4,3,2,2,1,1,0],
					[0,1,2,2,3,4,5,5,5,4,3,2,2,2,1,0],
					[0,1,2,3,4,5,5,5,4,4,3,2,2,2,1,0],
					[0,1,2,3,4,4,4,4,3,3,2,2,1,1,1,0],
					[0,1,1,2,3,3,3,3,2,2,2,2,1,1,1,0],
					[0,0,1,1,2,2,2,2,2,2,2,1,1,1,0,0],
					[0,0,0,1,1,1,2,2,2,1,1,1,1,0,0,0],
					[0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],
					[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

#monariza
animation_array1 = [
					[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 1, 1, 2, 2, 1, 1, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 1, 1, 2, 2, 1, 1, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 1, 1, 2, 2, 1, 1, 1, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 1, 1, 2, 2, 1, 1, 1, 0, 0, 0, 0],
					[0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 0, 0],
					[0, 0, 0, 1, 1, 1, 1, 2, 3, 2, 1, 1, 1, 1, 0, 0],
					[0, 0, 0, 1, 1, 1, 2, 2, 3, 2, 2, 2, 1, 1, 0, 0],
					[0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 3, 2, 1, 1, 0, 0],
					[0, 0, 1, 1, 1, 2, 2, 3, 2, 2, 2, 2, 1, 1, 0, 0],
					[0, 0, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0],
					[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
					[0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
					]

for i in range(1, 256):
	x = i % 16
	z = i // 16
	bpy.ops.object.select_all(action='TOGGLE')
	bpy.data.objects['pin_body'].select = True
	bpy.ops.object.duplicate()
	bpy.ops.transform.translate(value=(x*0.2999389,0,z*0.2999389))
	
	#set the keyframes
	#frame: 0, ,60, 120~130 → 0
	#frame: 24~36, 84~96 → 1
	bpy.context.scene.frame_set(0)
	bpy.ops.anim.keyframe_insert_menu(type="Location")
	bpy.context.scene.frame_set(60)
	bpy.ops.anim.keyframe_insert_menu(type="Location")
	bpy.context.scene.frame_set(80)
	bpy.ops.anim.keyframe_insert_menu(type="Location")

	# bpy.context.scene.frame_set(120)
	# bpy.ops.anim.keyframe_insert_menu(type="Location")
	# bpy.context.scene.frame_set(130)
	# bpy.ops.anim.keyframe_insert_menu(type="Location")

	bpy.context.scene.frame_set(24)
	bpy.ops.transform.translate(value=(0,-animation_array1[x][15-z]*0.4,0))
	bpy.ops.anim.keyframe_insert_menu(type="Location")
	bpy.context.scene.frame_set(36)
	bpy.ops.transform.translate(value=(0,-animation_array1[x][15-z]*0.4,0))
	bpy.ops.anim.keyframe_insert_menu(type="Location")

	# bpy.context.scene.frame_set(84)
	# bpy.ops.transform.translate(value=(0,-animation_array2[x][15-z]*0.4,0))
	# bpy.ops.anim.keyframe_insert_menu(type="Location")
	# bpy.context.scene.frame_set(96)
	# bpy.ops.transform.translate(value=(0,-animation_array2[x][15-z]*0.4,0))
	# bpy.ops.anim.keyframe_insert_menu(type="Location")
