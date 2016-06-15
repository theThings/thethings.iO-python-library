
Welcome to thethingsAPI's documentation!
****************************************

Contents:

class class thethingsAPI.TheThingsAPI(token=None)

   activate(actCode)

      Activates a non activated thing.

      Args:
         actCode: activation code string.

      Returns:
         true on sucess, False on malformed URL error.  Any network
         problem raises an exception.

      Raises:
         URLError on errors (from urllib2.urlopen)

   activateSync(resource, act, auxResource=None)

      Turn on or off sync mechanism for subscribe. If sync is on,
      every time the class realises that  the connection is lost, it
      will query thethings.io to recover lost data for a single
      specific resource.

      An auxiliary resource is needed to know which is the last
      processed data. i.e. Once internet connection is recovered, Sync
      will check the timestamp of the auxiliar  resource (by default
      resource + "_ack") and the timestamp  of the last value written
      for the specific resource  that we want to recover lost data
      ("resource" argument  of this function). If the timestamps
      differe, the  subscribe thread will recover all the data between
      this  two timestamps and will place it in the suscribe queue.
      Therefore, is the task of the user to: (a) Manually add a
      timestamp when writting the resource that we want to monitor
      (using third argument of addVar function). (b) Update the
      auxiliary resource with the timestamp  of the last processed
      data. Otherwise, Sync may  read an already processed value and
      put it again  in the subscribe queue (to stash multiple data
      from  once, it's enough to upddate the auxiliary resource  with
      the oldest data). The function stashData can be used for this
      purpose. In summary, if Sync is on, after processing a value
      read from the subscribe queue, the function "stashData" should
      be called with the value of the timestamp of the readed value.

      Args:
         resource: resource that we want to recover
            data if the connection is lost or the application is
            closed.

         auxResource: name of the auxiliary resource.

   addVar(key, value, dt=None)

      Add the pair {key : value} to the list of pending  data to be
      written to thethings.io. This function can  be called any times
      to add more variables to be sent.  Call the "write" function to
      actually write the values.

      Args:
         key: string key to write. value: value dt: custom timestamp
         either string '2015-10-28T12:18:56.799Z' or python datetype.

   clear()

      Clear internal data buffer to be written

   static dt2str(dt)

      Converts datetime python object to formated string.

      Args:
         dt: python datetime

      Returns:
         string '2015-10-28T12:18:56.799Z'.

   getToken()

      Get function for internal token.

      Returns:
         current token.

   internalLogs(act)

      set on or off internal logs of this class that will provide
      information for developers. The logs will be written to
      thethings.io resources  "err" and "log" for errors and other
      logs  respectively.

      Args:
         act: true if on, false if off.

   read(key, limit=1, startDate=None, endDate=None, to=10)

      Read a variable from the theThings.iO. If only the  argument
      "key" is specified, the last value will be  returned. This
      function will return "limit" number of  values of the variable
      inside an array. The elements are returned from newest to oldest

      Args:
         key: name of the variable limit: max number of values to
         return. startDate: '2015-10-28T12:18:56.799Z' or datetime
         endDate: '2015-10-28T12:18:56.799Z' or datetime to: timeout
         in seconds

      Returns:
         None on connection timeout, 0 if the resource  doesn't exist,
         otherwise a list with the readed  values.

   stashData(dt)

      Stash data up to dt datetime as processed. This function is only
      useful for the Sync feature. It won't return until the data has
      been written.

      Args:
         dt: datetime python object.

   static str2dt(strdate)

      Converts a formated string to python datetime.

      Args:
         strdate: string '2015-10-28T12:18:56.799Z'.

      Returns:
         datedime python object.

   subscribe()

      Subscribe to thethings.iO. Calling this function will start a
      thread that will listen for incoming data from thethings.iO and
      will queue it as it is  retrieved.

      Returns:
         A python queue to read the data.

   write()

      Actually write the values to theThings.iO. See  function
      "addVar". internal list of data to be sent is cleared.

      Returns:
         Http code status

      Raises:
         URLError on errors (from urllib2.urlopen)


Indices and tables
******************

* *Index*

* *Module Index*

* *Search Page*
