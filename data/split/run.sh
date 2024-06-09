awk '{f="datasplit" NR; print $0 " -|"> f}' RS='-\\|'  data.txt

awk '{f="summaries" NR; print $0 " -|"> f}' RS='<td><span class="emptyspace">&nbsp;</span></td>'  1up29en-al-qaida.html
               <td><span class="emptyspace">&nbsp;</span></td>

