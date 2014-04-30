import consensus, listener, threading, custom, blockchain, leveldb, gui, networking
DB=leveldb.LevelDB(custom.database_name)
todo=[[consensus.mainloop, (custom.pubkey, custom.peers, custom.hashes_per_check, DB), False],
      [listener.server, (DB, ), False],
      [gui.main, (custom.gui_port, custom.brainwallet, DB), False]]
#we also need a gui
networking.kill_processes_using_ports([str(custom.gui_port),str(custom.listen_port)])

for i in todo:
    t = threading.Thread(target=i[0], args = i[1])
    t.setDaemon(i[2])
    t.start()




