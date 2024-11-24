import scom
import cfgmgr
import proto
import partitioner

cmgr = cfgmgr.config_manager(file_path='conf.json')
scm = scom.scom(cmgr)

src_ident = proto.ident.generate()
pack = proto.packet.create(src_ident, proto.ident.generate(), proto.packet.tds_s.flag_cont(255), 0)

psds_cmp = pack.psds.compile()
psds_data = psds_cmp.data()
vals = partitioner.get_values(psds_data)

for x in vals:
    if(partitioner.is_partition(x)):
        for y in partitioner.get_values(x):
            if(partitioner.is_partition(y)):
                for z in partitioner.get_values(y):
                    print(f'-- {z}')

            else: print(f'- {y}')
    else: print(f'{x}')
    print('\n\n')
