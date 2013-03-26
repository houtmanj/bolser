__author__ = 'jos'


import datasource
import argparse
import evoque
import evoque.domain


def action_list(args):
    print args
    domain = evoque.domain.Domain("/Users/jos/Documents/bolser/templates")
    t = domain.get_template(args.output, quoting="str")
    print t.evoque({'selected_systems': selected_systems})
    print "action_list"


def action_mon(args):
    print "action_mon"
    domain = evoque.domain.Domain("/Users/jos/Documents/bolser/templates")
    t = domain.get_template(args.output, quoting="str")
    print t.evoque({'selected_systems': selected_systems})
    pass

def action_serv(args):
    print "action_serv"
    domain = evoque.domain.Domain("/Users/jos/Documents/bolser/templates")
    t = domain.get_template(args.output, quoting="str")
    print t.evoque({'selected_systems': selected_systems})
    pass


parser = argparse.ArgumentParser(description='Bol.com System information', fromfile_prefix_chars='@')
#parser.set_defaults(func=action_list)

parser.add_argument('-o', '--output', '--ou', default="default", help='select a template for the output')
parser.add_argument('--verbose', '-v', action='count', help="increase verbosity level")

group1 = parser.add_argument_group('system selection modifiers', 'These arguments modify the system selection')
group1.add_argument('-s', '--systemname', action="append",
    help='specify a systemname')
group1.add_argument('-r', '--role', action='append', help='specify a systemrole')

group1.add_argument('-t', '--test', '--tst', dest='environment',
    action='append_const', const='test', help='select systems in the environment: test')
group1.add_argument('-a', '--acceptence', '--acc', dest='environment',
    action='append_const', const='acceptence', help='select systems in the environment: acceptence')
group1.add_argument('-x', '--preproduction', '--xpr', dest='environment',
    action='append_const', const='preproduction', help='select systems in the environment: preproduction')
group1.add_argument('-p', '--production', '--prod', dest='environment',
    action='append_const', const='production', help='select systems in the environment: production')

group1.add_argument('--all', action='store_true', default=False, help='select all systems, does not work with other modifiers')


subparsers = parser.add_subparsers(help='sub-command help')
parser_list = subparsers.add_parser('list', help='list systems information')
parser_list.set_defaults(func=action_list)

parser_mon = subparsers.add_parser('mon', help='monitoring help')
parser_mon.add_argument('--ack', metavar="service-name", help='acknowledge a service')
parser_mon.set_defaults(func=action_mon)


parser_serv = subparsers.add_parser('serv', help='service help')
parser_serv.add_argument('--restart', action="store_true", default="store_false", help='restart a service')
parser_serv.add_argument('--stop', action="store_true", default="store_false", help='stop a service')
parser_serv.add_argument('--start', action="store_true", default="store_false", help='start a service')
parser_serv.set_defaults(func=action_serv)


args = parser.parse_args()
data = datasource.JsonDatasource()

selection_criteria = {}

if args.all:
    args.environment = ['test', 'acceptence', 'preproduction', 'production']

if args.systemname is not None:
    selection_criteria['systemname']=args.systemname

if args.role is not None:
    selection_criteria['role']=args.role

if args.environment is not None:
    selection_criteria['environment']=args.environment

selected_systems =  data.getSystem(**selection_criteria)

args.func(args)
