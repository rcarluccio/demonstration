var get_cell_style_html = function(cell_style){
    if (cell_style == "split")
        {return "float:left; width:50%;";}
    return "width:100%;";
    };

var update_cell_style_element = function(cell){
    var cell_style_html = get_cell_style_html(cell.metadata.cell_style);
    cell.element.attr('style', cell_style_html);
    };

function initialise(cells, ncells){
    for (var i=0; i<ncells; i++){
        var cell = cells[i];
        if ("cell_style" in cell.metadata){
            update_cell_style_element(cell, cell.metadata.cell_style);
            }
        }
    }

$(document).ready(
    function(){
        $('div.input').hide();
        var cells = Jupyter.notebook.get_cells();
        var ncells = Jupyter.notebook.ncells();
        initialise(cells, ncells);
        }
    )