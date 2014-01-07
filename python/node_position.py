import nuke

def align(nodes, axis='x'):

    axis_string = '{0}pos'.format(axis)
    nodes = sorted(nodes, key=lambda x: x[axis_string].value())
    position = nodes[0][axis_string].value()

    for node in nodes:
        node[axis_string].setValue(position)

def space_evenly(nodes, axis='x'):

    nodes = sorted(nodes, key=lambda x: x['xpos'].value())
    xpos = nodes[0]['xpos'].value()

    axis_string = '{0}pos'.format(axis)
    dimension = 'Width'
    if axis == 'y':
        dimension = 'Height'

    node_dimensions = 0
    positions = []
    for node in nodes:
        position = node[axis_string].value()
        node_dimension = eval('node.screen{0}'.format(dimension))()
        node_dimensions += node_dimension
        positions.append(position)
        positions.append(position + node_dimension)

    min_pos = min(positions)
    max_pos = max(positions)

    total_dimensions = max_pos - min_pos
    empty_space = total_dimensions - node_dimensions
    spacing = empty_space/(len(nodes) - 1)

    previous_node = nodes[0]
    for node in nodes[1:]:
        ppos = previous_node[axis_string].value()
        pdimension = eval('node.screen{0}'.format(dimension))()
        new_pos = ppos + pdimension + spacing
        node[axis_string].setValue(new_pos)
        previous_node = node

