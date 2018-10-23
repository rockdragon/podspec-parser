Pod::Spec.new do |s|
  s.name          = 'ExampleApp'
  s.version       = '1.0.1'
  s.author        = { 'Author' => 'author@app.com' }
  s.license       = 'MIT'
  s.homepage      = 'https://github.com/author/example-app/tree/master/'
  s.summary       = 'Example App For Parser'
  s.source        = { :git => 'ssh://github.com/author/example-app', :tag => s.version.to_s }

  s.platform      = :ios
  s.ios.deployment_target = '9.0'
  s.static_framework = true
  s.pod_target_xcconfig = { 'SWIFT_VERSION' => '4.0' }

  s.dependency 'SnapKit', '~> 4.0'
  s.dependency 'RxSwift', '4.0.0'
  s.dependency 'RxCocoa', '4.0.0'
  s.dependency 'RxDataSources', '~> 3.0'
  s.dependency 'ExampleFoundation', '~> 1.2.0'
  s.dependency 'ExampleUIKit', '~> 1.5.0'
  s.dependency 'ExampleModel'
  s.dependency 'ExampleRustClient'
  s.dependency 'ExampleRustHeaders'
  s.dependency 'Swinject'
  s.dependency 'ExampleContainer'

  s.source_files = 'ExampleContact/Source/*.swift'
  s.resource_bundles = {
    'ExampleContact' => ['ExampleContact/Resources/*']
  }
end
