# Review

Review is an app for reviewing python apps.

## Developing

```sh
git clone https://github.com/jeffknupp/review.git
cd review
virtualenv --no-site-packages venv
source venv/bin/activate
pip install -r requirements.txt
```

### Testing

Run all tests:

    $ nosetest

Run all tests with coverage:

    $ nosetests --with-coverage

Run some particular test:

    $ nosetests review.test
    $ nosetests review.test:test_simple
