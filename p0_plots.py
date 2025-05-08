import pandas as pd
import numpy as np
from lets_plot import *

LetsPlot.setup_html(isolated_frame=True)

from palmerpenguins import load_penguins
df = load_penguins()
cell2_1 = (
  ggplot(
    data = df,
    mapping = aes(
      x = "flipper_length_mm",
      y = "body_mass_g",
    ))
  + geom_point()
)


cell2_2 = (
  ggplot(
    data = df,
    mapping = aes(
      x = "flipper_length_mm",
      y = "body_mass_g",
      color = "species",
    ))
  + geom_point()
)

cell2_3 = (
  ggplot(
    data = df,
    mapping = aes(
      x = "flipper_length_mm",
      y = "body_mass_g",
      color = "species",
    ))
  + geom_point()
  + geom_smooth(method = "lm")
)


cell2_4 = (
  ggplot(
    data = df,
    mapping = aes(
      x = "flipper_length_mm",
      y = "body_mass_g",
    ))
  + geom_point(mapping = aes(
    color = "species",
    ))
  + geom_smooth(method = "lm")
)

cell2_5 = (
  ggplot(
    data = df,
    mapping = aes(
      x = "flipper_length_mm",
      y = "body_mass_g",
    ))
  + geom_point(mapping = aes(
    color = "species",
    shape = "species",
    ))
  + geom_smooth(method = "lm")
)

cell2_6 = cell2_5 = (
  ggplot(
    data = df,
    mapping = aes(
      x = "flipper_length_mm",
      y = "body_mass_g",
    ))
  + geom_point(mapping = aes(
    color = "species",
    shape = "species",
    ))
  + geom_smooth(method = "lm")
  + labs(
    title = "Body mass and flipper length",
    subtitle = "Dimensions for Adelie, Chinstrap, and Gentoo penguins",
    x="Flipper length (mm)",
    y="Body mass (g)",
    color="Species",
    shape="Species",
  )
)