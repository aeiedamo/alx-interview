#!/usr/bin/python3
"""
  You have n number of locked boxes in front of you.
  Each box is numbered sequentially from 0 to n - 1
  and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
  """
    function to check the unlock-ability of the boxes.
  """
  if not isinstance(boxes, list):
    return False
  elif len(boxes) == 0:
    return False


  for key in range(1, len(boxes) - 1):
    boxes_checked = False

    for i in range(len(boxes)):
      boxes_checked = key in boxes[i] and i != key
      if boxes_checked:
        break

    if boxes_checked is False:
      return boxes_checked

  return True
