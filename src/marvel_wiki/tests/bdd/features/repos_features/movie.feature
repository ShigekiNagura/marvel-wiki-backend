Feature: 映画情報に関するテスト

Scenario Outline: 映画情報を登録する
    Given ユースケースのインスタンス化
    When title=<title>, summary=<summary>, published_at=<published_at>の映画情報を登録する
    Then データを取得する

    Examples: movies
        | title           | summary                                                                 | published_at |
        | アイアンマン      | トニースタークがアイアンマンとなり、自身の会社の開発した武器を悪用する敵を倒す       | 2008-09-27    |
        | アイアンマン11    | アイアンマンの11作品目                                                      | 2022-05-07    |

Scenario: 映画情報を更新する
    Given ユースケースのインスタンス化
    When update_movieを呼び出す
    Then データを取得する

Scenario: 映画情報を取得する
    Given ユースケースのインスタンス化
    When get_moviesを呼び出す
    Then データを取得する

Scenario Outline: 映画情報を削除する
    Given ユースケースのインスタンス化
    When delete_movieを呼び出し、id=<id>を削除

    Examples: ids
        | id    |
        | 1     |
        | 2     |