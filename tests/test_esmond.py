import logging

from esmond_helper import esmond

from tests import data

logging.basicConfig(level=logging.INFO)


def test_esmond_group_by_participants(mocked_test_redis):
    """
    sanity test on group_by_participants

    test data contains non-zero number of participants
    :param mocked_test_redis: mocked redis connection
    """

    tests = esmond.load_tests(
        data.ESMOND_BASE_URL,
        mocked_test_redis)
    num_participants = 0
    for g in esmond.group_by_participants(tests):
        logging.info("participants: " + str(g["participants"]))
        logging.info("  num tests: %d" % len(g["tests"]))
        num_participants += 1

    assert num_participants > 0, \
        "test data contained participiants, but none found"


def test_esmond_group_by_tool(mocked_test_redis):
    """
    sanity test on group_by_tool

    test data contains non-zero number of tools
    :param mocked_test_redis: mocked redis connection
    """

    tests = esmond.load_tests(
        data.ESMOND_BASE_URL,
        mocked_test_redis)
    num_tools = 0
    for name, tests in esmond.group_by_tool(tests).items():
        logging.info("'%s': %d tests" % (name, len(tests)))
        num_tools += 1

    assert num_tools > 0, "test data contained tools, but none found"
