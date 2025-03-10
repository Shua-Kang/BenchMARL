#  Copyright (c) Meta Platforms, Inc. and affiliates.
#
#  This source code is licensed under the license found in the
#  LICENSE file in the root directory of this source tree.
#

from dataclasses import dataclass, MISSING


@dataclass
@dataclass
class TaskConfig:
    task: str = MISSING
    max_cycles: int = MISSING
    map_id: int = MISSING
    reward_setting: str = MISSING
    dense_rewards_setting: dict = MISSING
