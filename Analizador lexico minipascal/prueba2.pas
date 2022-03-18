program teclado;
uses crt;

var codigo: integer;

begin
    clrscr;
    writeln(''codigo ascii');   (*error intensional*)
    write('Ingrese codigo (0-255): ');  
    readln(codigo);
    writeln;
    writeln('codigo: ',codigo);
    writeln('signo: ', chr(codigo));
    readkey;
end. 