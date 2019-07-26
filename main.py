from k8s import list, connect


def main():
    k8s = connect.get_k8s_core_client()
    list.test(k8s)
    # miq = get_miq_client()
    #
    # for user in miq.collections.users.all:
    #     print(user.userid)
    #
    # pprint(miq.collections)
    #
    # for p in miq.collections.all_names:
    #     pprint(p)
    #
    # pprint(miq.collections.alert_definitions)
    # for ad in miq.collections.alert_definitions:
    #     pprint(vars(ad.action))
    #     pprint(ad.action)
    #
    # ad = miq.collections.alert_definitions[5]
    # pprint(ad.guid)
    # pprint(ad.action)

    # miq.collections.alert_definitions[27].action.delete()
    # miq.collections.policies.action.create({"name":"Test","description":"Test",
    #                                         "mode":"control", "towhat":"ContainerImage",
    #                                         "condition_ids":[], "policy_contents":[],
    #                                         "conditions_ids":[]})


if __name__ == "__main__":
    main()
