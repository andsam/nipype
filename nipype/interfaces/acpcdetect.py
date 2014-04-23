from nipype.interfaces.base import (
    TraitedSpec,
    CommandLineInputSpec,
    CommandLine,
    File
)
import os

class ACPCDInputSpec(CommandLineInputSpec):
    input_file = File(desc="Infile", exists=True, mandatory=True, argstr="-i %s")

class ACPCDOutputSpec(TraitedSpec):
    output_file = File(desc = "Outfile", exists = True, argstr='-o ac_%s')

class ACPCDTask(CommandLine):
    input_spec = APCPDInputSpec
    output_spec = ACPCDOutputSpec
    cmd = 'acpcdetect'

    def _list_outputs(self):
            outputs = self.output_spec().get()
            outputs['output_file'] = os.path.abspath("ac_" + self.inputs.input_file)
            return outputs

if __name__ == '__main__':

    acd = ACPCDTask(input_file='an_existing_file')
    print acd.cmdline
    acd.run()
