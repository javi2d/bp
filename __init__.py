
import sys

import bpy
import mdl

import inspect


def register():

	print( 'Register bp module' )


def link( __mod__ , cls ):

	for k,v in vars(cls).items():

		if inspect.isfunction(v):

			def wrapper( *args , **kwargs ):
				
				c = getattr( __mod__ , cls.__name__ )

				m = getattr( c , k )

				return n( *args , **kwargs )


			print( 555 , k )

			setattr( cls , k , wrapper )







# def panel( cls ):

# 	print( cls.__name__ )

# 	module = inspect.getmodule( sys._getframe( 1 ) )

# 	ctx = {}

# 	for k,v in vars(cls).items():

# 		# print( k , v )

# 		# print( inspect.ismethod(v) , inspect.isfunction(v) )

# 		if inspect.isfunction(v):

# 			def other_draw( self , context ):

# 				getattr( module , '__name__' )

# 				return getattr( cls , 'draw' )( self , context )


# 			ctx[k] = other_draw

# 		else:

# 			ctx[k] = v




# 	op_class = type( cls.__name__, (bpy.types.Panel, ) ,ctx )
# 	bpy.utils.register_class(op_class)	

# 	return cls