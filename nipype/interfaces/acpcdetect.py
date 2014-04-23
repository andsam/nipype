from nipype.interfaces.base import (
    TraitedSpec,
    CommandLineInputSpec,
    CommandLine,
    File
)
from nipype.interfaces.traits_extension import isdefined
import os

class ACPCInputSpec(CommandLineInputSpec):
    infile = File(desc="Infile", exists=True, mandatory=True, argstr='-i %s')
    outname = File(genfile=True, desc="outfile", position= -1, argstr='-o %s')

class ACPCOutputSpec(TraitedSpec):
    outfile = File(desc = "Outfile", exists = True)

class ACPCDetect(CommandLine):
    input_spec = ACPCInputSpec
    output_spec = ACPCOutputSpec
    cmd = 'acpcdetect'

    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['outfile'] = self.inputs.outname
        if not isdefined(outputs['outfile']):
            outputs['outfile'] = os.path.abspath(self._gen_outfilename())
        else:
            outputs['outfile'] = os.path.abspath(outputs['outfile'])
        return outputs

    def _gen_filename(self, name):
        if name is 'outname':
            return self._gen_outfilename()
        else:
            return None

    def _gen_outfilename(self):
        name = os.path.basename(self.inputs.infile)
        return 'ac_' + name 

if __name__ == '__main__':

    acd = ACPCDetect(infile='an_existing_file')
    print acd.cmdline
    acd.run()
