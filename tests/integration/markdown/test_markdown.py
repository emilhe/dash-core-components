import pytest
from selenium.common.exceptions import WebDriverException
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html


def test_mkdw001_display(dash_dcc):
    app = dash.Dash(__name__)

    app.layout = html.Div(
        [
            html.Div(['Markdown link']),
            dcc.Markdown(['[Title](title_crumb)']),
            html.Div(['Markdown dccLink']),
            dcc.Markdown(['<dccLink href="title_crumb" children="Title" />']),
            html.Div(['Markdown dccLink - explicit children']),
            dcc.Markdown(
                [
                    '''
            <dccLink href="title_crumb">
                Title
            </dccLink>
        '''
                ]
            ),
            html.Div('Markdown dccLink - nested image'),
            dcc.Markdown(
                [
                    '''
            <dccLink href="title_crumb">
                <img src="assets/image.png" />
            </dccLink>
        '''
                ]
            ),
            html.Div('Markdown dccLink - nested markdown'),
            dcc.Markdown(
                [
                    '''
            <dccLink href="title_crumb">
                <dccMarkdown children="## Title" />
            </dccLink>
        '''
                ]
            ),
            html.Div('Markdown dccLink - nested markdown image'),
            dcc.Markdown(
                [
                    '''
            <dccLink href="title_crumb">
                <dccMarkdown children="![Image](assets/image.png)" />
            </dccLink>
        '''
                ]
            ),
        ]
    )

    dash_dcc.start_server(app)
    dash_dcc.percy_snapshot("mkdw001 - markdowns display")
