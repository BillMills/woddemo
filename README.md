## wodpy demo

A toy usage of the new [wodpy pacakge](https://github.com/BillMills/wodpy) for reading World Ocean Dataset data. A bunch of ways you can help out:

#### Does it install?

 1. Clone this repo: `git clone https://github.com/BillMills/woddemo.git; cd woddemo`
 2. Install `wodpy`: `sudo pip install wodpy`
 3. Run this demo: `python demo.py`
 4. Did it print 61.93?
  - Yes: Great! Installation has worked. Open an issue, tell me your operating system version and python version, and that things seem ok.
  - No: Something has gone wrong with installation. Please open an issue, cut and paste in any error messages you got, and tell me your operating system version and python version. Thanks!

#### Do the tests pass for you?
 
 1. Clone the development repo for wodpy: `git clone https://github.com/IQuOD/wodpy.git; cd wodpy`
 2. Run the tests: `nosetests`
 3. Do they all pass?
  - Yes: Awesome!
  - No: Cut and paste the errors you get into an issue in this repo, and tell me your operating system version and python version. Thanks!

#### For the ocean science inclined:

 We will be using this pacakge to unpack data for IQuOD's [AutoQC](https://github.com/IQuOD/AutoQC) project, but I'd like feedback on how things go using `wodpy` in other projects. Are all the necessary features there? Any bugs? Is usage convenient and easy to learn? Let me know in an issue here or in the [wodpy repo](https://github.com/BillMills/wodpy).
