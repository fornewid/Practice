items = '이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,' \
        '이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌'\
        .split(',')

def count_by_last_name(items, last_name):
    return len([x for x in items if x.startswith(last_name)])
print('1. 김씨와 이씨는 각각 몇 명 인가요?\n %d명, %d명'
      % (count_by_last_name(items, '이'), count_by_last_name(items, '김')))

print('2. "이재영"이란 이름이 몇 번 반복되나요?\n %d번'
      % items.count('이재영'))

print('3. 중복을 제거한 이름을 출력하세요.\n', set(items))

print('4. 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.\n',
      sorted(set(items)))
