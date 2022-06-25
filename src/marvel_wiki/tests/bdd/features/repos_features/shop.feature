Feature: 店舗情報取得に関する振る舞い

Scenario: ホームページでランダムに5店舗の情報を取得できる
    Given: なし
    When: get_random_shopsを呼び出す
    Then: 5店舗取得できる

Scenario: 店舗カテゴリーごとの件数を取得できる
    Given: なし
    When: get_shops_by_categoryに<category>を渡して呼び出す
    Then: <count>店舗取得できる

    Examples: Sweets Category
        | cateogry | count |
        | cake     | 5     |
        | pancake  | 3     |

Scenario: 店舗一覧で「もっと見る」をクリックすると、追加で10個の店舗情報が表示される
    Given: なし
    When: offsetを<11>,limitを<10>でget_shops_by_categoryを呼び出す
    Then: 10店舗取得できる
